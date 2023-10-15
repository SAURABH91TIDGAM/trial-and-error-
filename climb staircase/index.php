<?php

function ways($m)
{
    $num1 = 0;
    $num2 = 1;

    for ($i = 0; $i < $m; $i++) {
        $result = $num1 + $num2;
        $num1 = $num2;
        $num2 = $result;
         
    }
    return $result;
}    
function climbStairs($n) 
{ 
    $ways = ways($n - 1) + ways($n - 2);
    echo $ways."\n";
}


climbStairs(5);


