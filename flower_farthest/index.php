<?php

$flower_garden = ["Dock", "Arum", "Yew", "Rue", "Ivy", "Ivy", "Rue", "Yew", "Arum", "Dock", "Iris", "Lily", "Reed", "Rose", "Sage", "Dock"];



$distance = 0;

if (sizeof($flower_garden) == 0)
{
    $distance = -1;
} elseif (sizeof($flower_garden) == 1) {
    
    $distance = -1;
}


for ($i = 0; $i < sizeof($flower_garden); $i++)
{

    for ($j = 1; $j < sizeof($flower_garden); $j++) {
        if ($flower_garden[$i] == $flower_garden[$j]) {
            $postion_difference = $j - $i;
            if ($postion_difference > $distance) {
                $distance = $postion_difference;
            }
        }
    }
}

echo $distance;
