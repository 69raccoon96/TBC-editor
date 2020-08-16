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
    public partial class Form1 : Form
    {
        public static List<string> textToDoc = new List<string>();
        private int selectedItem;
        public static Resources res = new Resources();
        public Form1()
        {
            InitializeComponent();
        }

        private void Button1_Click(object sender, EventArgs e)
        {
            var textForm = new Text(this, res.persons);
            textForm.ShowDialog();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void ListBox1_MouseDown(object sender, MouseEventArgs e)
        {
            int index = this.listBox1.IndexFromPoint(e.Location);
            if (index != ListBox.NoMatches)
            {
                selectedItem = index;
                if (e.Button == MouseButtons.Left)
                {
                    var menu = new ContextMenuStrip();
                    menu.Items.Add("Удалить");
                    menu.Items[0].Click += new EventHandler(DeleteClicked);
                    menu.Show(Cursor.Position);
                }
            }
            
        }
        private void DeleteClicked(object sender,EventArgs e)
        {
            Converter.RemoveItem(selectedItem);
            listBox1.Items.RemoveAt(selectedItem);
        }
        private void ListBox1_ouseClick(object sender, MouseEventArgs e)
        {

        }

        private void Button2_Click(object sender, EventArgs e)
        {
            var choosePerson = new ChoosePeron(res.persons,this);
            choosePerson.Show();
        }

        private void Button5_Click(object sender, EventArgs e)
        {
            Converter.SaveFile();
        }
    }
}
