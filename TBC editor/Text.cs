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
        private List<Person> persons;
        readonly Form1 form;
        public Text(Form1 form, List<Person> res)
        {
            this.form = form;
            persons = res;
            InitializeComponent();
        }

        private void Text_Load(object sender, EventArgs e)
        {
            comboBox1.Items.AddRange(persons.Select(x => x.Name).ToArray());
        }

        private void Button1_Click(object sender, EventArgs e)
        {
            if(textBox1.TextLength == 0)
            {
                MessageBox.Show("Пожалуйста, добавьте текст, который произносит персонаж");
                return;
            }
            int person;
            try
            {
                person = comboBox1.SelectedIndex;
            }
            catch
            {
                MessageBox.Show("Пожалуйста выберите, кто произносит фразу");
                return;
            }
            var text = persons[person].Tag + " \"" + textBox1.Text + "\"";
            Form1.textToDoc.Add(text);
            form.listBox1.Items.Add(persons[person].Name + " \"" + textBox1.Text + "\"");
            textBox1.Clear();
        }

        private void Button2_Click(object sender, EventArgs e)
        {
            Close();
        }
    }
}
