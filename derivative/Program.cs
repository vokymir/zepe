class Program
{

    public static void Main(string[] args)
    {
        Console.WriteLine(Derivate(Math.Sin, Math.PI));
        Console.WriteLine(DerivateSine(Math.PI));

    }

    /// <summary>
    /// Calulate the derivative of the function in paramref name="x".
    /// Uses the basic derivative formula of "(f(x+h) - f(x)) / h" - where h is chosen to be arbitrarily small.
    /// Works in double precision.
    /// </summary>
    /// <param name="f"> Any mathematical function to take derivative of. Should be defined in paramref name="x" - this function won't check that.</param>
    /// <param name="x"> Value of x, in which the derivative of f(x) will be calculated.</param>
    public static double Derivate(Func<double, double> f, double x)
    {
        double h = 1e-16;
        return (f(x + h) - f(x)) / h;
    }

    /// <summary>
    /// Calculate the derivative of Sine in paramref name="x".
    /// Uses the genius "Sin(a+b) = Sin(a)Cos(b) + Cos(a)Sin(b)" formula for better precision.
    /// </summary>
    /// param name="x"> Value of x in which to caluclate the derivative. </param>
    public static double DerivateSine(double x)
    {
        double h = 1e-16;
        return (Math.Sin(x) * Math.Cos(h) + Math.Cos(x) * Math.Sin(h) - Math.Sin(x)) / h;
    }
}
