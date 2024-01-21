using System;
using System.Linq;


namespace MyApplication
{
  class Program
  {

    static void MainMethod()
    {  
      // Type your username and press enter
      Console.WriteLine("Enter username:");
      // Create a string variable and get user input from the keyboard and store it in the variable
      string userName = Console.ReadLine();
      Console.WriteLine("enter value:");
      string value = Console.ReadLine();
      // Another mathode 
      int value2 = Convert.ToInt32(Console.ReadLine());
      // Print the value of the variable (userName), which will display the input value
      Console.WriteLine("Username is: " + userName);
      Console.WriteLine("value: " + Convert.ToInt32(value));
      Console.WriteLine("value2: " + value2);
      // trying int + oparator
      int sum1 = 5+10,
      sum2= sum1 + 10,
      sum3= sum2 + sum1;
      int sum4= 5;
      sum4+=10; 
      
      Console.WriteLine("sum value: "+sum1);
      Console.WriteLine("sum2 : "+ sum2);
      Console.WriteLine("sum3 : "+sum3);
      Console.WriteLine("sum4 : "+sum4); 
      Console.WriteLine("hello world");  
      string txt = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
      Console.WriteLine("The length of the txt string is: " + txt.Length); 

      string firstName = "John";
      string lastName = "Doe";
      string name = $"My full name is:{firstName} {lastName}";
      Console.WriteLine(name); 
      if(firstName.Length<lastName.Length)
      {
        Console.WriteLine("error");
      }
      else
      {
        Console.WriteLine("here");
      } 

    }
    static void MyMethod(string value = "here")
    {
      Console.WriteLine(value);
      Console.WriteLine(value+112);

    }
    static void framMethod(string fram)
    {
      Console.WriteLine(fram + "World");
    }

    static void Main(string[] args)
    {
      int[] myNumbers = {5, 1, 8, 9};
      Console.WriteLine(myNumbers.Max());  // returns the largest value
      Console.WriteLine(myNumbers.Min());  // returns the smallest value
      Console.WriteLine(myNumbers.Sum());  // returns the sum of elements

     // MainMethod();
     // MyMethod();
     // MyMethod("hello there");
     // framMethod("Hello");
      
      Myclass myObj = new Myclass();
      Console.WriteLine(myObj.color);
      Console.WriteLine(myObj.color1);
     // Console.WriteLine();
     // mainfun();
      Myclass.mainfun();
      
    }
  }
}
