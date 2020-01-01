using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace TBC_editor
{
    public partial class Images : Form
    {
        public Images()
        {
            InitializeComponent();
        }

        private void Images_Load(object sender, EventArgs e)
        {
            string test = "";
            foreach(var image in Form1.images)
            {
                test += image + " ";
            }
            label1.Text = test;
        }
    }
}
