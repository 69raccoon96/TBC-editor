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
        List<Bitmap> images;
        string name;
        public Images(List<Bitmap> images, string name)
        {
            InitializeComponent();
            this.images = images;
            this.name = name;
        }

        private void Images_Load(object sender, EventArgs e)
        {
            var x = 10;
            var y = 10;
            var count = 0;
            foreach(var image in images)
            {
                var pb = new PictureBox();
                pb.Image = image;
                pb.Size = new Size(100, 100);
                pb.SizeMode = PictureBoxSizeMode.StretchImage;
                pb.Location = new Point(x, y);
                pb.DoubleClick += new EventHandler(ImageClicked);
                this.Controls.Add(pb);
                x += 105;
                count++;
                if(count == 3)
                {
                    count = 0;
                    y += 105;
                    x -= 105 * 3;
                }
               
            }
        }
        private void ImageClicked(object sender,EventArgs e)
        {
            var image = (Bitmap)((Button)sender).Image;
            if(name == "body")
            {
                ChoosePeron.body = image;
            }

        }
    }
}
