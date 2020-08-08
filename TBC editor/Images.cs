using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace TBC_editor
{
    public partial class Images : Form
    {
        private static Dictionary<string,string> persons = new Dictionary<string,string>();
        public Images()
        {
            InitializeComponent();
            persons.Add("dv", "Алиса");
        }

        private void Images_Load(object sender, EventArgs e)
        {
            DirectoryInfo dir = new DirectoryInfo(Directory.GetCurrentDirectory() + "\\images\\sprites\\");
            var files = dir.GetFiles();
            label1.Text = "";
            foreach(var elem in files)
            {
                label1.Text += elem.Name + "\n";
            }
        }
    }
}
