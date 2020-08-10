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
            var point = listBox1.Location;
            point.Offset(listBox1.Width + 5,0);
            var button = new Button();
            button.Location = point;
            button.Size = new Size(100, 50);
            button.Text = "Тело";
            button.Click += new EventHandler(OpenBodies);
            Controls.Add(button);
        }
        private void OpenBodies(object sender, EventArgs e)
        {
            var images = new Images(persons[index].Bodies);
            images.Show();
        }
        private void ListBox1_MouseDown(object sender, MouseEventArgs e)
        {
            index = this.listBox1.IndexFromPoint(e.Location);
        }
    }
}
