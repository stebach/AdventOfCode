<?php
if (count($argv) < 2 || substr($argv[1], 0, 2) != "20" || strval(intval($argv[1])) != $argv[1]) {
    echo "please provide a valid year as argument!\n";
    die();
}
$year = intval($argv[1]);

$mainJavaFolder = __DIR__ . '/../src/main/java/li/ste/adventofcode/year' . $year . '/';
$mainResourceFolder = __DIR__ . '/../src/main/resources/' . $year . '/';
$testJavaFolder = __DIR__ . '/../src/test/java/li/ste/adventofcode/year' . $year . '/';
$testResourceFolder = __DIR__ . '/../src/test/resources/' . $year . '/';

foreach ([$mainJavaFolder, $mainResourceFolder, $testJavaFolder, $testResourceFolder] as $folder) {
    if (!file_exists($folder)) {
        mkdir($folder);
    }
}

$vars = ['{{YEAR}}' => $year];
for ($day = 1 ; $day < 26; $day++) {
    $paddedNumber = padNumber($day);
    $vars['{{DAY}}'] = $paddedNumber;
    file_put_contents($mainJavaFolder . 'Day' . $paddedNumber . '.java', parseTemplate('main_java.tpl', $vars));
    file_put_contents($mainResourceFolder . 'Day' . $paddedNumber . '.txt', '// TODO: get data!');
    file_put_contents($testJavaFolder . 'TestDay' . $paddedNumber . '.java', parseTemplate('test_java.tpl', $vars));
    file_put_contents($testResourceFolder . 'TestDay' . $paddedNumber . '.txt', '// TODO: get data!');
}

var_dump($year);

function padNumber($nr)
{
    return str_pad($nr, 2, "0", STR_PAD_LEFT);
}

function parseTemplate($file, $vars)
{
    $content = file_get_contents(__DIR__ . '/' . $file);
    return str_replace(
        array_keys($vars),
        array_values($vars),
        $content
    );
}
