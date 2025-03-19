using System.Diagnostics;

public class Program
{
    /// <summary>
    /// Test time differences between smart and dumb band matrix.
    /// All parameters of test are inside this class.
    /// </summary>
    public static void Main()
    {
        int n = 5000;
        int m = 5;
        int repeat = 100;
        Stopwatch sw = new Stopwatch();
        long[] t1 = new long[repeat];
        long[] t2 = new long[repeat];

        Console.WriteLine($"Measuring time difference between smart and dumb band matrix multiplication implementation.\nMatrix dimension: {n}x{n}\nBand width: {m}\nWill repeat {repeat} times.\nTime is measured in milliseconds.\n  RUN  | Dumb | Smart | Equals");

        for (int i = 0; i < repeat; i++)
        {
            var mat = SmartMatrix.generateMatrix(n, m);
            var v = Vector.GenerateVector(n);
            var dumat = new DumbMatrix(n, m, mat.data);

            sw.Restart();
            var res1 = mat * v;
            t1[i] = sw.ElapsedMilliseconds;

            sw.Restart();
            var res2 = dumat * v;
            t2[i] = sw.ElapsedMilliseconds;

            Console.WriteLine($"{(i + 1).ToString("000")}/{repeat.ToString("000")}| {t1[i].ToString("0000")} | {t2[i].ToString("0000")}  | {res1.Equals(res2)}");
        }

        Console.WriteLine($"\n###########\n# Average #\n###########\nDumb: {t1.Average()} ms \nSmart: {t2.Average()} ms");
    }
}

/// <summary>
/// Matrix represented by 2D array with all stored values - even zeroes.
/// </summary>
public class DumbMatrix
{
    public double[,] data { get; private set; }

    /// <param name="dim"> Dimension of matrix: dim x dim matrix.</param>
    /// <param name="bandWidth"> Width of band - if 1, only diagonal, if 2 on both sides add diagonal. Outside the band are only zeroes.</param>
    /// <param name="numbers"> Array of numbers which are in band - all other numbers are zeroes, so no need to give them.</param>
    public DumbMatrix(int dim, int bandWidth, double[] numbers)
    {
        data = new double[dim, dim];
        int ptrNumbers = 0;

        for (int i = 0; i < dim; i++)
        {
            for (int j = 0; j < dim; j++)
            {
                if (Math.Abs(j - i) < bandWidth)
                {
                    data[i, j] = numbers[ptrNumbers];
                    ptrNumbers++;
                }
            }
        }
    }
}

/// <summary>
/// Only stores significant numbers (these in the band).
/// </summary>
public class SmartMatrix
{
    public double[] data { get; private set; }
    public int dim { get; private set; }
    public int bandWidth { get; private set; }

    public SmartMatrix(int dim, int bandWidth, double[] numbers) => (data, this.dim, this.bandWidth) = (numbers, dim, bandWidth);

    /// <summary>
    /// For given [r]ow and [c]olumn return value - indexer from data to matrix coordinates.
    /// </summary>
    public double getData(int r, int c)
    {
        // if the element is outside the band, we know its 0
        if (Math.Abs(c - r) >= bandWidth)
            return 0;

        int index = 0;

        // sum the number of stored elements from rows 0 up to r-1
        for (int i = 0; i < r; i++)
        {
            int rowStart = Math.Max(0, i - (bandWidth - 1));
            int rowEnd = Math.Min(dim - 1, i + (bandWidth - 1));
            int count = rowEnd - rowStart + 1;
            index += count;
        }

        // offset in row
        int currentRowStart = Math.Max(0, r - (bandWidth - 1));
        int offset = c - currentRowStart;
        index += offset;

        return data[index];
    }

    /// Generate smart matrix of random numbers inside bandWidth from 0 to upperBound.
    public static SmartMatrix generateMatrix(int dim, int bandWidth, double upperBound = 1000.0)
    {
        int length = (2 * bandWidth - 1) * dim - bandWidth * (bandWidth - 1);
        double[] data = new double[length];
        Random r = new Random();

        for (int i = 0; i < length; i++)
        {
            data[i] = r.NextDouble() * upperBound;
        }

        return new SmartMatrix(dim, bandWidth, data);
    }
}

public class Vector
{
    public double[] values { get; set; }

    public Vector(double[] values) => this.values = values;
    public Vector(int length) => this.values = new double[length];

    /// <summary>
    /// Generates new vector of given length with random numbers between 0 and range.
    /// </summary>
    public static Vector GenerateVector(int length, double range = 1000)
    {
        double[] values = new double[length];
        Random r = new Random();

        for (int i = 0; i < length; i++)
        {
            values[i] = r.NextDouble() * range;
        }

        return new Vector(values);
    }

    /// <summary>
    /// Print the vector in WolframAlpha-friendly format, as 1 column matrix.
    /// </summary>
    public override string ToString()
    {
        string s = "{";

        for (int i = 0; i < this.values.Length - 1; i++)
        {
            s += $"{{{this.values[i].ToString("0.00")}}},";
        }

        s += $"{{{this.values[this.values.Length - 1].ToString("0.00")}}}}}";

        return s;
    }

    /// <summary>
    /// Check value by value if are equal.
    /// </summary>
    public override bool Equals(object? obj)
    {
        if (obj is not Vector) return false;

        int length = this.values.Length;
        if (length != ((Vector)obj).values.Length) return false;

        // arbitrary value, precision of comparison
        double epsilon = 1e-10;

        for (int i = 0; i < length; i++)
        {
            double item1 = this.values[i];
            double item2 = ((Vector)obj).values[i];
            if (Math.Abs(item1 - item2) > epsilon) return false;
        }

        return true;
    }

    public override int GetHashCode()
    {
        return this.values.Length;
    }

    /// Matrix-vector multiplication.
    public static Vector operator *(DumbMatrix m, Vector v)
    {
        Vector res = new Vector(v.values.Length);

        for (int i = 0; i < v.values.Length; i++)
        {
            double sum = 0;

            for (int j = 0; j < v.values.Length; j++)
            {
                sum += m.data[i, j] * v.values[j];
            }

            res.values[i] = sum;
        }
        return res;
    }

    /// Matrix-vector multiplication.
    public static Vector operator *(SmartMatrix m, Vector v)
    {
        Vector res = new Vector(v.values.Length);

        for (int i = 0; i < v.values.Length; i++)
        {
            double sum = 0;

            for (int j = 0; j < v.values.Length; j++)
            {
                sum += m.getData(i, j) * v.values[j];
            }

            res.values[i] = sum;
        }
        return res;
    }
}
