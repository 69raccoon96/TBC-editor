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
        ChoosePeron cp;
        public Images(List<Bitmap> images, string name,ChoosePeron cp)
        {
            InitializeComponent();
            this.images = images;
            this.name = name;
            this.cp = cp;
        }

        private void Images_Load(object sender, EventArgs e)
        {
            this.AutoScroll = true;
            var x = 10;
            var y = 10;
            var count = 0;
            foreach(var image in images)
            {
                if(name != "body")
                {
                    var tag = ((string)image.Tag).Split(' ');
                    string cur;
                    if (tag.Length == 2 || tag[2] == "far")
                        cur = "1";
                    else
                        cur = tag[2];
                    if (cur != ChoosePeron.currentPos)
                        continue;
                }
                var pb = new PictureBox
                {
                    Image = image,
                    Size = new Size(100, 100),
                    SizeMode = PictureBoxSizeMode.StretchImage,
                    Location = new Point(x, y)
                };
                pb.DoubleClick += new EventHandler(ImageClicked);
                var label = new Label();
                label.Text = (string)image.Tag;
                label.Location = new Point(x, y + 105);
                this.Controls.Add(label);
                this.Controls.Add(pb);
                x += 105;
                count++;
                if(count == 3)
                {
                    count = 0;
                    y += 105 + label.Height;
                    x -= 105 * 3;
                }
               
            }
        }
        private void ImageClicked(object sender,EventArgs e)
        {
            var image = (Bitmap)((PictureBox)sender).Image;
            if (name == "body")
            {
                ChoosePeron.body = image;
                var tag = ((string)image.Tag).Split(' ');
                if(tag.Length == 2 || tag[2] == "far")
                {
                    ChoosePeron.currentPos = "1";
                }else
                {
                    ChoosePeron.currentPos = tag[2];
                }
            }
            if (name == "clothes")
                ChoosePeron.clothes = image;
            if (name == "emotions")
                ChoosePeron.emotion = image;
            cp.Invalidate();
            foreach (var button in cp.Controls.OfType<Button>())
            {
                button.Enabled = true;
            }
        }
    }
}
