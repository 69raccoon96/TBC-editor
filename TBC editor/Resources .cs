using System;
using System.Collections.Generic;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace TBC_editor
{
    public struct Person
    {
        public string Name;
        public string Tag;
        public string Color;
        public Person(params string[] ps)
            {
            Name = ps[0];
            Tag = ps[1];
            Color = ps[2];
            }
    }
    public class Resources
    {
        public List<Person> persons = new List<Person>();
        public List<Bitmap> images = new List<Bitmap>();
        public Resources()
        {
            var path = Directory.GetCurrentDirectory() + "\\persons.txt";
            using (StreamReader sr = new StreamReader(path))
            {
                while(!sr.EndOfStream)
                {
                    var vars = sr.ReadLine().Split(' ');
                    if (vars.Length != 3)
                        continue;
                    var person = new Person(vars);
                    persons.Add(person);
                }
            }
        }
    }
}
