docker build -f Dockerfile -t "kubtmp" .
chmod +x kubtmp.sh
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null && pwd )"
ln -sf "$DIR/kubtmp.sh" /usr/local/bin/kubtmp