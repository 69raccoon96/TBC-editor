﻿using System;
using System.Collections.Generic;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace TBC_editor
{
    public class Person
    {
        public string Name;
        public string Tag;
        public string Color;
        public List<Bitmap> Bodies = new List<Bitmap>();
        public List<Bitmap> Emotions = new List<Bitmap>();
        public List<Bitmap> Clothes = new List<Bitmap>();
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
            path = Directory.GetCurrentDirectory() + "\\images\\sprites\\";
            DirectoryInfo dir = new DirectoryInfo(path);
            var files = dir.GetFiles();
            foreach(var person in persons)
            {
                foreach(var file in files)
                {
                    if(file.Name.Contains(person.Tag+"_"))
                    {
                        if (file.Name.Contains("telo"))
                        {
                            person.Bodies.Add(new Bitmap(path + "\\" + file.Name));
                            continue;
                        }
                        if (file.Name.Contains("pion") || file.Name.Contains("ulica") || file.Name.Contains("swim"))
                        {
                            person.Clothes.Add(new Bitmap(path + "\\" + file.Name));
                            continue;
                        }
                        person.Emotions.Add(new Bitmap(path + "\\" + file.Name));
                    }
                }
            }
            var a = persons;
        }
    }
}