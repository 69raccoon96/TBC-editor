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
        int indexToMove;
        public static List<string> textToDoc = new List<string>();
        private int selectedItem;
        public static Resources res = new Resources();
        public Form1()
        {
            InitializeComponent();
            listBox1.AllowDrop = true;

            //подписываемся на события
            listBox1.MouseMove += new MouseEventHandler(listBox1_MouseMove);
            listBox1.DragEnter += new DragEventHandler(listBox1_DragEnter);
            listBox1.DragDrop += new DragEventHandler(listBox1_DragDrop);

        }
        private void listBox1_MouseMove(object sender, MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Left)
            {
                indexToMove = listBox1.IndexFromPoint(e.X, e.Y);
                listBox1.DoDragDrop(indexToMove, DragDropEffects.Move);
            }
        }

        private void listBox1_DragEnter(object sender, DragEventArgs e)
        {
            e.Effect = DragDropEffects.Move;
        }

        private void listBox1_DragDrop(object sender, DragEventArgs e)
        {
            
            int newIndex = listBox1.IndexFromPoint(listBox1.PointToClient(new Point(e.X, e.Y)));
            Converter.ReplaceLines(indexToMove, newIndex);
            //если вставка происходит в начало списка
            if (newIndex == -1)
            {
                
                //получаем перетаскиваемый элемент
                object itemToMove = listBox1.Items[indexToMove];
                //удаляем элемент
                listBox1.Items.RemoveAt(indexToMove);
                //добавляем в конец списка
                listBox1.Items.Add(itemToMove);
            }
            //вставляем где-то в середину списка
            else if (indexToMove != newIndex)
            {
                //получаем перетаскиваемый элемент
                object itemToMove = listBox1.Items[indexToMove];
                //удаляем элемент
                listBox1.Items.RemoveAt(indexToMove);
                //вставляем в конкретную позицию
                listBox1.Items.Insert(newIndex, itemToMove);
            }
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
                if (e.Button == MouseButtons.Right)
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

        private void Button3_Click(object sender, EventArgs e)
        {
            var form = new BG(res.bg);
            form.Show();
        }
    }
}
