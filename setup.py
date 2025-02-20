{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "ddc7ee51-4758-4000-9897-b33cdcf0281a",
   "metadata": {},
   "outputs": [
    {
     "ename": "FileNotFoundError",
     "evalue": "[Errno 2] No such file or directory: 'README.md'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mFileNotFoundError\u001b[0m                         Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[2], line 9\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01msetuptools\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m setup, find_packages\n\u001b[0;32m      3\u001b[0m setup(\n\u001b[0;32m      4\u001b[0m     name\u001b[38;5;241m=\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mmani\u001b[39m\u001b[38;5;124m'\u001b[39m,\n\u001b[0;32m      5\u001b[0m     version\u001b[38;5;241m=\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124m1.0.0\u001b[39m\u001b[38;5;124m'\u001b[39m,\n\u001b[0;32m      6\u001b[0m     author\u001b[38;5;241m=\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mYour Name\u001b[39m\u001b[38;5;124m'\u001b[39m,\n\u001b[0;32m      7\u001b[0m     author_email\u001b[38;5;241m=\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124myour_email@example.com\u001b[39m\u001b[38;5;124m'\u001b[39m,\n\u001b[0;32m      8\u001b[0m     description\u001b[38;5;241m=\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mA high-performance scientific and statistical computing library\u001b[39m\u001b[38;5;124m'\u001b[39m,\n\u001b[1;32m----> 9\u001b[0m     long_description\u001b[38;5;241m=\u001b[39m\u001b[38;5;28mopen\u001b[39m(\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mREADME.md\u001b[39m\u001b[38;5;124m'\u001b[39m)\u001b[38;5;241m.\u001b[39mread(),\n\u001b[0;32m     10\u001b[0m     long_description_content_type\u001b[38;5;241m=\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mtext/markdown\u001b[39m\u001b[38;5;124m'\u001b[39m,\n\u001b[0;32m     11\u001b[0m     url\u001b[38;5;241m=\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mhttps://github.com/yourusername/mani\u001b[39m\u001b[38;5;124m'\u001b[39m,  \u001b[38;5;66;03m# GitHub repository link\u001b[39;00m\n\u001b[0;32m     12\u001b[0m     packages\u001b[38;5;241m=\u001b[39mfind_packages(),\n\u001b[0;32m     13\u001b[0m     classifiers\u001b[38;5;241m=\u001b[39m[\n\u001b[0;32m     14\u001b[0m         \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mProgramming Language :: Python :: 3\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     15\u001b[0m         \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mLicense :: OSI Approved :: MIT License\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     16\u001b[0m         \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mOperating System :: OS Independent\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     17\u001b[0m     ],\n\u001b[0;32m     18\u001b[0m     python_requires\u001b[38;5;241m=\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124m>=3.6\u001b[39m\u001b[38;5;124m'\u001b[39m,\n\u001b[0;32m     19\u001b[0m )\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\IPython\\core\\interactiveshell.py:324\u001b[0m, in \u001b[0;36m_modified_open\u001b[1;34m(file, *args, **kwargs)\u001b[0m\n\u001b[0;32m    317\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m file \u001b[38;5;129;01min\u001b[39;00m {\u001b[38;5;241m0\u001b[39m, \u001b[38;5;241m1\u001b[39m, \u001b[38;5;241m2\u001b[39m}:\n\u001b[0;32m    318\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mValueError\u001b[39;00m(\n\u001b[0;32m    319\u001b[0m         \u001b[38;5;124mf\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mIPython won\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mt let you open fd=\u001b[39m\u001b[38;5;132;01m{\u001b[39;00mfile\u001b[38;5;132;01m}\u001b[39;00m\u001b[38;5;124m by default \u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    320\u001b[0m         \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mas it is likely to crash IPython. If you know what you are doing, \u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    321\u001b[0m         \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124myou can use builtins\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124m open.\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    322\u001b[0m     )\n\u001b[1;32m--> 324\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m io_open(file, \u001b[38;5;241m*\u001b[39margs, \u001b[38;5;241m*\u001b[39m\u001b[38;5;241m*\u001b[39mkwargs)\n",
      "\u001b[1;31mFileNotFoundError\u001b[0m: [Errno 2] No such file or directory: 'README.md'"
     ]
    }
   ],
   "source": [
    "from setuptools import setup, find_packages\n",
    "\n",
    "setup(\n",
    "    name='mani',\n",
    "    version='1.0.0',\n",
    "    author='Manikant_Rajput',\n",
    "    author_email='manikantsing123@gmail.com',\n",
    "    description='A high-performance scientific and statistical computing library',\n",
    "    long_description=open('README.md').read(),\n",
    "    long_description_content_type='text/markdown',\n",
    "    url='https://github.com/Manikant10/mani-library',  # GitHub repository link\n",
    "    packages=find_packages(),\n",
    "    classifiers=[\n",
    "        \"Programming Language :: Python :: 3\",\n",
    "        \"License :: OSI Approved :: MIT License\",\n",
    "        \"Operating System :: OS Independent\",\n",
    "    ],\n",
    "    python_requires='>=3.6',\n",
    ")\n"
   ]
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
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
