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
    public partial class Text : Form
    {
        private static Dictionary<string, string> persons = new Dictionary<string, string>();
        Form1 form;
        public Text(Form1 form)
        {
            this.form = form;
            InitializeComponent();
        }

        private void Text_Load(object sender, EventArgs e)
        {
            persons.Add("Славя", "sl");
            persons.Add("Лена", "le");
            persons.Add("Алиса", "dv");
            comboBox1.Items.AddRange(persons.Keys.ToArray());
        }

        private void Button1_Click(object sender, EventArgs e)
        {
            var person = comboBox1.SelectedItem.ToString();
            var text = persons[person] + " \"" + textBox1.Text + "\"";
            Form1.textToDoc.Add(text);
            form.listBox1.Items.Add(person + " \"" + textBox1.Text + "\"");
        }

        private void Button2_Click(object sender, EventArgs e)
        {
            this.Close();
        }
    }
}
