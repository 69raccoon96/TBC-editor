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
        Form1 form;
        public static string currentPos;
        int index;
        public ChoosePeron(List<Person> persons, Form1 form)
        {
            this.form = form;
            this.persons = persons;
            InitializeComponent();
        }

        private void ChoosePeron_Load(object sender, EventArgs e)
        {
            for(var i = 0; i < persons.Count; i++)
            {
                listBox1.Items.Add(persons[i].Name);
            }
            listBox1.SelectedIndex = 0;
            index = 0;
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
            point.Offset(105, 0);
            action = PickSprite;
            CreateButton(point, "Выбрать", action);
            this.Width = point.X + 180;
        }
        
        private void CreateButton(Point point, string text, Action<object,EventArgs> action)
        {
            var button = new Button();
            button.Location = point;
            button.Size = new Size(100, 50);
            button.Text = text;
            button.Click += new EventHandler(action);
            if (text == "Одежда" || text == "Эмоция" || text == "Выбрать")
                button.Enabled = false;
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
        private void PickSprite(object sender, EventArgs e)
        {
            Converter.AddSprite((string)body.Tag, (string)clothes.Tag, (string)emotion.Tag, "");
            form.listBox1.Items.Add("Спрайт: " + GetCurrentName());
            body = null;
            emotion = null;
            clothes = null;
            Close();
        }
        public string GetCurrentName()
        {
            foreach(var person in persons)
            {
                foreach(var currentBody in person.Bodies)
                {
                    if ((string)currentBody.Tag == (string)body.Tag)
                        return person.Name;
                }
            }
            throw new ArgumentException();
        }
        private void ListBox1_MouseDown(object sender, MouseEventArgs e)
        {
            int lastIndex = index;
            index = this.listBox1.IndexFromPoint(e.Location);
            if (lastIndex != index)
            {
                foreach (var button in Controls.OfType<Button>())
                    if (button.Text != "Тело")
                        button.Enabled = false;
                body = null;
                emotion = null;
                clothes = null;
                Invalidate();
            }

        }

        private void ChoosePeron_Paint(object sender, PaintEventArgs e)
        {
                Graphics g = e.Graphics;
                if (body != null)
                {
                    DrawImage(g,body);
                }
                if (clothes != null)
                {
                    DrawImage(g, clothes);
                }
                if (emotion != null)
                {
                    DrawImage(g, emotion);
                }
        }
        private void DrawImage(Graphics g,Bitmap image)
        {
            var size = new Size(image.Width / 2, image.Height / 2);
            var bodyFixed = new Bitmap(image, size);
            var rect = new Rectangle(listBox1.Width + 5, 55, size.Width,size.Height);
            g.DrawImage(bodyFixed, rect);
        }
    }
}
