using System;

namespace MyApplication
{
    class Myclass
    {
        //public string color = "red my color", color1 = "red";
        public string color = "red my color";
        public string color1 = "red";
        public static void mainfun()
        {
            Console.WriteLine("hello im here!!");
            classPrg myObj2 = new classPrg();
            Console.WriteLine(myObj2.color+"--"+myObj2.color1);
            classPrg.mainfun();
        }


    }
}