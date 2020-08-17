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
    public partial class BG : Form
    {
        Form1 form;
        Background bg;
        int index = 0;
        public BG(Background bg, Form1 form)
        {
            InitializeComponent();
            this.form = form;
            this.AutoScroll = true;
            this.bg = bg;
        }
        private void UpdateForm()
        {
            var comboBox1 = new ComboBox();
            comboBox1.Items.AddRange(new object[] { "Внутри", "Снаружи", "ЦГ" });
            comboBox1.SelectedIndex = index;
            comboBox1.Name = "cb";
            comboBox1.SelectedIndexChanged += new EventHandler(IndexChanged);
            comboBox1.Size = new Size(121, 24);
            comboBox1.Location = new Point(12, 12);
            Controls.Add(comboBox1);
            var current = new List<Bitmap>();
            if (index == 0)
                current = bg.Inside;
            if (index == 1)
                current = bg.Outside;
            var point = comboBox1.Location;
            point.Offset(0, 20);
            var count = 0;
            foreach(var image in current)
            {
                var pb = new PictureBox();
                pb.Size = new Size(300, 200);
                pb.Location = point;
                pb.Image = image;
                pb.SizeMode = PictureBoxSizeMode.StretchImage;
                pb.DoubleClick += new EventHandler(PBClicked);
                Controls.Add(pb);
                point.Offset(305, 0);
                count++;
                if(count == 5)
                {
                    count = 0;
                    point.Offset(-(5 * 305), 205);
                }
            }
        }
        private void Background_Load(object sender, EventArgs e)
        {
            
            UpdateForm();
            
        }
        private void IndexChanged(object sender, EventArgs e)
        {
            var curIndex = ((ComboBox)sender).SelectedIndex;
            if (curIndex != -1)
            {
                index = curIndex;
                Controls.Clear();
                UpdateForm();
            }
        }
        private void PBClicked(object sender, EventArgs e)
        {
            var name = (string)((PictureBox)sender).Image.Tag;
            Converter.AddBg(name);
            form.listBox1.Items.Add("Задний фон:" + name.Substring(3));
            Close();
        }
    }
}
