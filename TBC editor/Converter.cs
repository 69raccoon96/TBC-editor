using System;
using System.Collections.Generic;
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
        public static void AddSprite(string body, string clothes, string emotions, string pos)
        {
            var text = "";
            if (pos.Length == 0)
            {
                text += "show " + body + "\n";
                text += "show " + clothes + "\n";
                text += "show " + emotions;
            }else
            {
                text += "show " + body + " at " + pos + "\n";
                text += "show " + clothes + " at " + pos + "\n";
                text += "show " + emotions + " at " + pos;
            }
            actions.Add(text);
        }
    }
}
