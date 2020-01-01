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
            int height = 400, width = 200;
            int x = 0, y = 0, diff = 10;
            foreach (string fName in Form1.images)
            {
                Image img = Image.FromFile(Form1.pathImages + "\\" + fName);
                PictureBox pb = new PictureBox();
                pb.Size = new Size(width, height);
                pb.SizeMode = PictureBoxSizeMode.StretchImage;
                pb.Image = img;
                if (x > 2 * diff + 2 * width)
                {
                    x = 0;
                    y += height + diff;
                }
                else
                {
                    x += width + diff;
                }
                pb.Location = new Point(x, y);
                x += diff;

                panel1.Controls.Add(pb);
            }
        }
    }
}
