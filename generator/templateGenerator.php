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

if (!file_exists('local.cooke.txt')) {
    echo "NO COOKIE FILE (local.cookie.txt)\n";
    die();
}
$cookie = trim(file_get_contents('local.cookie.txt'));

for ($day = 1 ; $day < 26; $day++) {
    echo "day " . $day . "\n";
    $paddedNumber = padNumber($day);
    $vars['{{DAY}}'] = $paddedNumber;
    file_put_contents($mainJavaFolder . 'Day' . $paddedNumber . '.java', parseTemplate('main_java.tpl', $vars));
    file_put_contents($mainResourceFolder . 'Day' . $paddedNumber . '.txt', getResource($year, $day, $cookie));
    file_put_contents($testJavaFolder . 'TestDay' . $paddedNumber . '.java', parseTemplate('test_java.tpl', $vars));
    file_put_contents($testResourceFolder . 'TestDay' . $paddedNumber . '.txt', '// TODO: get data!');
    sleep (2);
}

var_dump($year);

function padNumber($nr)
{
    return str_pad($nr, 2, "0", STR_PAD_LEFT);
}

function getResource($year, $day, $cookie) {
    $url = 'https://adventofcode.com/' . $year . '/day/' . $day . '/input';

    $curl = curl_init();

    curl_setopt_array($curl, array(
        CURLOPT_URL => $url,
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_ENCODING => '',
        CURLOPT_MAXREDIRS => 10,
        CURLOPT_TIMEOUT => 0,
        CURLOPT_FOLLOWLOCATION => true,
        CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
        CURLOPT_CUSTOMREQUEST => 'GET',
        CURLOPT_HTTPHEADER => array(
          'Cookie: session=' . $cookie,
          'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
          'Referer: ' . substr($url, 0, -6),
        ),
    ));

    $response = curl_exec($curl);
    $data = $response;

    curl_close($curl);

    return trim($data);
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
