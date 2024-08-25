{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "51455870-1e28-49db-9415-454eed8ef8d7",
   "metadata": {},
   "outputs": [],
   "source": [
    "import smtplib\n",
    "#Simple Mail Tranfer Protocol\n",
    "#xyxq lopd nxxy tgka"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "d90be91b-e60f-48f2-a7c6-27204e0623ee",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "d0ff4679-1ef4-4af0-816e-2d9a90b3bb56",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "raw",
   "id": "595ae6cd-f768-4502-a1f8-3b7c7c8ae54f",
   "metadata": {},
   "source": [
    "import datetime"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "8d81ee52-1408-44a6-b610-882ea7e143dc",
   "metadata": {},
   "outputs": [],
   "source": [
    "import datetime"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "dc504b8b-1d65-4fcc-b26b-842a6e394cdf",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2024-08-25 09:41:57.641187\n"
     ]
    }
   ],
   "source": [
    "now = datetime.datetime.now()\n",
    "print(now)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "2775bdd7-96ba-4f66-8620-ff19b86a714a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2024\n"
     ]
    }
   ],
   "source": [
    "year = now.year\n",
    "print(year)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "87fe2195-ab21-497e-ac90-e58e95668286",
   "metadata": {},
   "source": [
    "### Boyfie Love Reminder"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "0d035014-4ed4-462e-b07f-ce8764682c2e",
   "metadata": {},
   "outputs": [],
   "source": [
    "import datetime\n",
    "import smtplib\n",
    "\n",
    "email = \"silvervoid3.14@gmail.com\"\n",
    "pwd = \"onhy wfny ueaw hrch\"\n",
    "\n",
    "now = datetime.datetime.now()\n",
    "weekday = now.weekday()\n",
    "\n",
    "with smtplib.SMTP(\"smtp.gmail.com\", 587) as con:\n",
    "    con.starttls()\n",
    "    con.login(user = email, password = pwd)\n",
    "    if(weekday == 6):\n",
    "        con.sendmail(from_addr = email, \n",
    "                     to_addrs = \"adistrange2004@gmail.com\", \n",
    "                     msg = \"Subject:Hi Babu\\n\\nBabu this is sent from python\\nI love you so much babu and I am Python Master. So I can tell you everyday, or everyweek, or every second too!! But i will not clog your emails, so, I'll tell you once in a week. I love you Adi Babu.\\nMuah\") \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "e1c921ef-813c-4e6c-a674-337de0a9e674",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "6\n"
     ]
    }
   ],
   "source": [
    "weekday = now.weekday()\n",
    "print(weekday)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "11317f78-ada9-48cb-bcf9-12ee901da46a",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
