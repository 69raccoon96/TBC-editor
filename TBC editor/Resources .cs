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
        public List<Bitmap> Bodies;
        public List<Bitmap> Emotions;
        public List<Bitmap> Clothes;
        public Person(params string[] ps)
        {
            Name = ps[0];
            Tag = ps[1];
            Color = ps[2];
            Bodies = new List<Bitmap>();
            Emotions = new List<Bitmap>();
            Clothes = new List<Bitmap>();
        }
    }
    public struct Background
    {
        public List<Bitmap> Inside;
        public List<Bitmap> Outside;

    }
    public class Resources
    {
        public List<Person> persons = new List<Person>();
        public Background bg = new Background();
        public Resources()
        {
            bg.Inside = new List<Bitmap>();
            bg.Outside = new List<Bitmap>();
            var path = Directory.GetCurrentDirectory() + "\\persons.txt";
            using (var sr = new StreamReader(path))
            {
                while (!sr.EndOfStream)
                {
                    var vars = sr.ReadLine().Split(' ');
                    if (vars.Length != 3)
                        continue;
                    var person = new Person(vars);
                    persons.Add(person);
                }
            }
            path = Directory.GetCurrentDirectory() + "\\images\\sprites\\";
            DirectoryInfo dir = new DirectoryInfo(path);
            var files = dir.GetFiles();
            foreach (var person in persons)
            {
                foreach (var file in files)
                {
                    if (file.Name.Substring(0, person.Tag.Length + 1) != person.Tag + "_")
                        continue;
                    var image = new Bitmap(path + "\\" + file.Name);
                    var tag = String.Join(" ", file.Name.Split('.')[0].Split('_').ToList());
                    image.Tag = tag;
                    if (file.Name.Contains("telo"))
                    {
                        person.Bodies.Add(image);
                        continue;
                    }
                    if (file.Name.Contains("pion") || file.Name.Contains("ulica") || file.Name.Contains("sport") || file.Name.Contains("swim") || file.Name.Contains("dress"))
                    {
                        person.Clothes.Add(image);
                        continue;
                    }
                    person.Emotions.Add(image);
                }
            }
            path = Directory.GetCurrentDirectory() + "\\images\\bg\\";
            dir = new DirectoryInfo(path);
            files = dir.GetFiles();
            foreach(var file in files)
            {
                var tag = String.Join(" ", file.Name.Split('.')[0].Split('_').ToList());
                var size = new Size(300, 200);
                var p = new Bitmap(path + "\\" + file.Name);
                var pic = new Bitmap(p, size);
                pic.Tag = tag;
                if (file.Name[0] == 'e')
                    bg.Outside.Add(pic);
                if(file.Name[0] == 'i')
                    bg.Inside.Add(pic);
            }
            var a = bg;
        }
    }
}
