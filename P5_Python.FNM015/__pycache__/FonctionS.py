o
    ^��c�  �                   @   s�  d d� Z dd� ZdZg ZeD ]Zed� ee� ee e�� eeed�� qdd� Zd	d
� Zg ZeD ]Zed� ee� eee�� eeed�� ed� q2dd� Zdd� Zg Z	ddl
Z
dd� Zdd� Ze	D ]#Zee�Ze�d�Zee� eeeed �eed �eed ��� qfdd� ZdD ]Zed� eeee�� ee� q�dZdZeegZeD ]]Ze�d�Zi ZeD ]Ze�d�Zed Zed ee< q�ee� eZeD ]7Zee �d�ee< ee d ee d d�ee< ee d �d �ee d< ee d! �d"d#�ee d!< eZq�q�ee ee< ee d ee d d�ee< ee d �d �ee d< ee d! �d"d#�ee d!< i Zee� eD ]6Zee �d�ee< ee d ee d d�ee< ee d �d �ee d< ee d! �d"d#�ee d!< �qBe e dS )$c                 C   s   | � � rdS dS �NTF)�isupper)�numero� r   �7/home/fatima/Sonatel-Academy/ProjectPython/FonctionS.py�	testUpper   s   r   c                 C   s   t | �|krdS dS r   )�len)r   �tailler   r   r   �
testTaille	   �   r	   �    z--------�   c                 C   �   | d � � rdS dS �Nr   TF��isalpha��chainer   r   r   �testPremierAlpha   r
   r   c                 C   �   t | �t| d�@ rdS dS )N�   TF�r   r	   )�prenomr   r   r   �
testPrenom/   �   r   r   c                 C   r   r   r   r   r   r   r   r   E   r
   c                 C   r   )N�   TFr   )�nomr   r   r   �testNomN   r   r   Nc                 C   s0   | � dd�� dd�� dd�� dd�� dd�} | S )N�mars�03�.�/�-�_� )�replacer   r   r   r   �sepDate_   s   ,r%   c                 C   s>   zt � t| �t|�t|��}d}W |S  ty   d}Y |S w r   )�datetime�int�
ValueError)�aa�mm�jour�newDate�correctDater   r   r   �dateCorrectee   s   ��r.   r    r   �   c                 C   s$   | d dv r| d � � dv rdS dS )Nr   )�3�4�5�6�����)�A�B�C�DTF)�upperr   r   r   r   �classeValide{   s   r:   r   z
----------�#�[�:)�devoirs�examenr>   �|r?   �]� )r   r	   �n�	testliste�i�printr   r   r   �	listeDater&   r%   r.   �splitr'   r:   �n1�n2�
listeNotes�note�dic�matierer   r$   r   r   r   r   �<module>   s�   	

	
*
	


� 