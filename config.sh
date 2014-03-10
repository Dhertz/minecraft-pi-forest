sudo /sbin/iptables -A OUTPUT -p udp --source-port 19132 -j DROP
echo iptables-persistent iptables-persistent/autosave_v4 boolean true | sudo debconf-set-selections
echo iptables-persistent iptables-persistent/autosave_v6 boolean true | sudo debconf-set-selections

sudo apt-get install -y git nodejs npm luakit iptables-persistent

sudo su -c 'iptables-save > /etc/iptables/rules.v4'

cd ..
git clone git://github.com/Dhertz/RPi-WaterbearNodeJS
cd RPi-WaterbearNodeJS
git submodule update --init --recursive
npm install --registry http://registry.npmjs.org
nodejs nodejs-server.js &
/home/pi/mcpi/minecraft-pi &
luakit -u http://localhost:8000/minecraftjs.html
