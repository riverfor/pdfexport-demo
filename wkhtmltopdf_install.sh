echo -e "\n---- Install WkHtmlToPdf 0.12.1 ----"
sudo wget https://downloads.wkhtmltopdf.org/0.12/0.12.5/wkhtmltox_0.12.5-1.xenial_amd64.deb
sudo dpkg -i wkhtmltox_0.12.5-1.xenial_amd64.deb
cd /usr/local/bin
sudo cp wkhtmltoimage /usr/bin/wkhtmltoimage
sudo cp wkhtmltopdf /usr/bin/wkhtmltopdf
echo -e "Wkhtmltopdf is installed!"
