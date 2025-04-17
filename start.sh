if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/HarshalPurohitEdits/kairnexbot.git /kairnexbot
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /kairnexbot
fi
cd /kairnexbot
pip3 install -U -r requirements.txt
echo "Starting kairnexbot...."
python3 bot.py
