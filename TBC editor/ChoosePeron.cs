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
            var images = new Images(persons[index].Bodies,"body");
            images.Show();
        }
        private void OpenEmo(object sender, EventArgs e)
        {
            var images = new Images(persons[index].Emotions,"emotions");
            images.Show();
        }
        private void OpenClothes(object sender, EventArgs e)
        {
            var images = new Images(persons[index].Clothes, "clothes");
            images.Show();
        }
        private void ListBox1_MouseDown(object sender, MouseEventArgs e)
        {
            index = this.listBox1.IndexFromPoint(e.Location);
        }
        public void UpdateImage()
        {
            groupBox1.Controls.Clear();

        }
    }
}
