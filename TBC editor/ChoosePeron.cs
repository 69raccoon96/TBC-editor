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
    public partial class ChoosePeron : Form
    {
        public static Bitmap body;
        public static Bitmap emotion;
        public static Bitmap clothes;
        List<Person> persons;
        int index;
        public ChoosePeron(List<Person> persons)
        {
            this.persons = persons;
            body = persons[0].Bodies[0];
            InitializeComponent();
        }

        private void ChoosePeron_Load(object sender, EventArgs e)
        {
            for(var i = 0; i < persons.Count; i++)
            {
                listBox1.Items.Add(persons[i].Name);
            }
            listBox1.SelectedIndex = 0;
            var point = listBox1.Location;
            point.Offset(listBox1.Width + 5,0);
            Action<object, EventArgs> action = OpenBodies;
            CreateButton(point, "Тело",action);
            action = OpenClothes;
            point.Offset(105, 0);
            CreateButton(point, "Одежда",action);
            point.Offset(105, 0);
            action = OpenEmo;
            CreateButton(point, "Эмоция",action);
        }
        
        private void CreateButton(Point point, string text, Action<object,EventArgs> action)
        {
            var button = new Button();
            button.Location = point;
            button.Size = new Size(100, 50);
            button.Text = text;
            button.Click += new EventHandler(action);
            Controls.Add(button);
        }
        private void OpenBodies(object sender, EventArgs e)
        {
            var images = new Images(persons[index].Bodies,"body",this);
            images.Show();
        }
        private void OpenEmo(object sender, EventArgs e)
        {
            var images = new Images(persons[index].Emotions,"emotions",this);
            images.Show();
        }
        private void OpenClothes(object sender, EventArgs e)
        {
            var images = new Images(persons[index].Clothes, "clothes",this);
            images.Show();
        }
        private void ListBox1_MouseDown(object sender, MouseEventArgs e)
        {
            index = this.listBox1.IndexFromPoint(e.Location);
        }

        private void ChoosePeron_Paint(object sender, PaintEventArgs e)
        {
            try
            {
                Graphics g = e.Graphics;
                if (body != null)
                {
                    var rect = new Rectangle(listBox1.Width + 5, 55, body.Width, body.Height);
                    g.DrawImage(body, rect);
                }
                if (clothes != null)
                {
                    var rect = new Rectangle(listBox1.Width + 5, 55, clothes.Width, clothes.Height);
                    g.DrawImage(clothes, rect);
                }
                if (emotion != null)
                {
                    var rect = new Rectangle(listBox1.Width + 5, 55, emotion.Width, emotion.Height);
                    g.DrawImage(emotion, rect);
                }
            }
            catch
            {
                return;
            }
        }
    }
}
