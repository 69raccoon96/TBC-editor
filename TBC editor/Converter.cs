using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace TBC_editor
{
    public class Converter
    {
        private static List<string> actions = new List<string>();
        
        public static void PersonSpeak(string person, string text)
        {
            actions.Add(person + " \"" + text + "\"");
        }
        public static void RemoveItem(int index)
        {
            actions.RemoveAt(index);
        }
        public static void AddBg(string bg)
        {
            bg = bg.Replace(' ', '_');
            actions.Add("scene bg " + bg);
        }
        public static void AddSprite(string body, string clothes, string emotions, string pos)
        {
            body = body.Replace(' ', '_');
            emotions = emotions.Replace(' ', '_');
            clothes = clothes.Replace(' ', '_');
            var text = "";
            if (pos.Length == 0 || pos == "По центру")
            {
                text += "show " + body + "\n";
                text += "show " + clothes + "\n";
                text += "show " + emotions;
            }else
            {
                text += "show " + body + " at " + GetCorrectPos(pos) + "\n";
                text += "show " + clothes + " at " + GetCorrectPos(pos) + "\n";
                text += "show " + emotions + " at " + GetCorrectPos(pos);
            }
            actions.Add(text);
        }
        public static void SaveFile()
        {
            var path = Directory.GetCurrentDirectory() + "\\result.txt";
            TextWriter tw = new StreamWriter(path);
            foreach (var s in actions)
                tw.WriteLine(s);
            tw.Close();
        }
        public static string GetCorrectPos(string pos)
        {
            if (pos == "Слева")
                return "left";
            if (pos == "Справа")
                return "right";
            return "";
        }
        public static void ReplaceLines(int index ,int newindex)
        {
            var elem = actions[index];
            actions.RemoveAt(index);
            if (newindex == -1)
                actions.Add(elem);
            else
                actions.Insert(newindex, elem);
        }
    }
}
