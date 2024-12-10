<?php

$programmingLanguages = ['Php', 'Python', 'C++'];

$programmingLanguages = [
    'php' => '10',
    'python' => '9'
];
$newLanguage = 'Go';
$programmingLanguages($newLanguage);

echo '<pre>';
print_r($programmingLanguages);
echo '</pre>';