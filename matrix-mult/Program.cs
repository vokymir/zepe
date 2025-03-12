using System.Diagnostics;

public class Program
{
    public static void Main(string[] args)
    {
        int n = 5000;
        int m = 5;
        double range = 1000;
        Stopwatch sw = new Stopwatch();
        Vector vector = Vector.GenerateVector(n, range);
        DumbMatrix matrix = DumbMatrix.GenerateMatrix(n, m, range);

        /*Console.WriteLine($"{matrix} * {vector}");*/

        sw.Start();
        Vector result = matrix * vector;
        long elapsed = sw.ElapsedMilliseconds;

        Console.WriteLine(elapsed);

        /*Console.WriteLine(result);*/
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
    public static Vector GenerateVector(int length, double range)
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
        double epsilon = 1e-16;

        for (int i = 0; i < length; i++)
        {
            double item1 = this.values[i];
            double item2 = ((Vector)obj).values[i];
            if (Math.Abs(item1 - item2) > epsilon) return false;
        }

        return true;
    }
}

public interface IBandMatrix<T> where T : IBandMatrix<T>
{
    // Generate Band matrix with random numbers in band. Matrix n*n, band width: m. The random numbers are between 0 and range.
    public static abstract T GenerateMatrix(int n, int m, double range);
    public static abstract Vector operator *(T m, Vector v);
}

public class DumbMatrix : IBandMatrix<DumbMatrix>
{
    double[,] values { get; set; }

    public DumbMatrix(int dim) => values = new double[dim, dim];

    public DumbMatrix(double[,] values) => this.values = values;

    /// <summary>
    /// Multiplies Matrix by Vector => returns Vector.
    /// </summary>
    public static Vector operator *(DumbMatrix m, Vector v)
    {
        int dim = m.values.GetLength(0);
        if (dim != m.values.GetLength(1) || dim != v.values.Length) throw new Exception("Matrix and Vector have either different dimensions, or Matrix isn't square.");
        Vector res = new Vector(dim);

        // For each row in matrix
        for (int i = 0; i < dim; i++)
        {
            double sum = 0;

            // Multiply each number in the matrix row by corresponding number in vector column and summ them all
            for (int j = 0; j < dim; j++)
            {
                sum += m.values[i, j] * v.values[j];
            }

            res.values[i] = sum;
        }

        return res;
    }

    /// <summary>
    /// Generate n*n matrix with zeroes except for random numbers (0 to range) on the diagonal band of width (m+1).
    /// </summary>
    public static DumbMatrix GenerateMatrix(int n, int m, double range)
    {
        double[,] values = new double[n, n];
        Random r = new Random();

        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                if (Math.Abs(i - j) < m)
                {
                    values[i, j] = r.NextDouble() * range;
                }
            }
        }

        return new DumbMatrix(values);
    }

    /// <summary>
    /// Print the matrix in WolframAlpha-friendly format.
    /// </summary>
    public override string ToString()
    {
        string s = "{";

        for (int i = 0; i < this.values.GetLength(0); i++)
        {
            s += $"{{{values[i, 0].ToString("0.00")},";
            for (int j = 1; j < this.values.GetLength(1) - 1; j++)
            {
                s += $"{values[i, j].ToString("0.00")},";
            }
            s += $"{values[i, this.values.GetLength(1) - 1].ToString("0.00")}}}{(i == this.values.GetLength(0) - 1 ? "" : ",")}";
        }

        s += "}";

        return s;
    }
}
