#!/bin/sh

source /lib/ar71xx.sh

NAME=""

case $(ar71xx_board_name) in
  yun)
    NAME="Yun"
  ;;
  nuy)
    NAME="Yun Shield"
  ;;
esac

echo "Content-type: text/html"
echo ""

echo '<html>'
echo '<head>'
echo '<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">'

echo  '<style>' \
      'body {'\
      '  background: #00979c;'\
      '  color: #222;'\
      '  font: 1em "Lucida Grande", Lucida, Verdana, sans-serif;'\
      '}'\
      'a,'\
      'a:link,'\
      'a:visited,'\
      'a:active,'\
      'a:hover {'\
      '  color: #222;'\
      '}'\
      '</style>'

echo '<title>Very first configuration page</title>'
echo '</head>'
echo '<body>'

echo "<h1>${NAME} First configuration</h1>"

echo "<h4>What is this page?"
echo "<br>You didn't follow the new and shiny Getting started flow, right? :)"
echo "<br>So now you should select a way to access the webpanel of your ${NAME}"
echo "<br>We strongly encourage using HTTPS Secure connection to protect your data"
echo "<br>If you choose to use HTTPS you'll also need to accept a certificate (the Getting started flow does it automatically)"
echo "<br>This choice screen will only be shown once</h4>"

echo "<form method=GET action=\"${SCRIPT}\">"

echo '<input type="radio" name="val_z" value="1" checked> Use HTTPS and make the web a better place<br>'\
     '<input type="radio" name="val_z" value="2"> I hate security, let me use old plain HTTP <br>'

echo '<br><input type="submit" value="Confirm"></form>'

# Make sure we have been invoked properly.

if [ "$REQUEST_METHOD" != "GET" ]; then
  echo "<hr>Script Error:"\
       "<br>Usage error, cannot complete request, REQUEST_METHOD!=GET."\
       "<br>Check your FORM declaration and be sure to use METHOD=\"GET\".<hr>"
  exit 1
fi

# If no search arguments, exit gracefully now.

if [ -z "$QUERY_STRING" ]; then
      exit 0
else
  # No looping this time, just extract the data you are looking for with sed:
  XX=`echo "$QUERY_STRING" | sed -n 's/^.*val_z=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
fi
echo '</body>'
echo '</html>'

if [ x$XX == x1 ]; then
  #using https, horray!
  cp /www/index.html.bak /www/index.html
  uci set uhttpd.main.redirect_https=1
  uci set arduino.@arduino[0].first_configuration=0
  uci commit
fi

if [ x$XX == x2 ]; then
  cp /www/index.html.bak /www/index.html
  uci set uhttpd.main.redirect_https=0
  uci set arduino.@arduino[0].first_configuration=0
  uci commit
fi

echo "<META HTTP-EQUIV=refresh CONTENT=\"4;URL=/cgi-bin/luci/webpanel/homepage\">"

/etc/init.d/uhttpd restart &

exit 0