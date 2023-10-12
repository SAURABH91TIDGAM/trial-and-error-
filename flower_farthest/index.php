<?php

function flower_farthest($flower_garden)
{
    $distance = 0;

    if (sizeof($flower_garden) == 0) {
        $distance -= 1;
    } elseif (sizeof($flower_garden) == 1) {

        $distance -= 1;
    } elseif (sizeof($flower_garden) == 2) {

        $distance -= 1;
    }


    for ($i = 0; $i < sizeof($flower_garden); $i++) {

        for ($j = 1; $j < sizeof($flower_garden); $j++) {
            if ($flower_garden[$i] == $flower_garden[$j]) {
                $postion_difference = $j - $i;
                if ($postion_difference > $distance) {
                    $distance = $postion_difference;
                }
            }
        }
        if ($i == sizeof($flower_garden) - 1 and $distance == 0) {
            $distance -= 1;
        }
    }

    echo $distance."\n"."\n\n";



}

flower_farthest($flower_garden = ["Ivy", "Rue", "Ivy", "Yew", "Rue", "Dock", "Iris", "Rue", "Lily"]);
flower_farthest($flower_garden = ["Rose"]);
flower_farthest($flower_garden = ["Ivy", "Rue", "Yew", "Arum", "Dock", "Iris", "Lily", "Reed", "Rose"]);
flower_farthest($flower_garden = ["Sage", "Rose", "Sage", "Reed", "Sage", "Lily", "Sage", "Iris", "Dock", "Sage", "Yew", "Rue", "Ivy"]);
flower_farthest($flower_garden = ["Dock", "Arum", "Yew", "Rue", "Ivy", "Ivy", "Rue", "Yew", "Arum", "Dock", "Iris", "Lily", "Reed", "Rose", "Sage", "Dock"]);
flower_farthest($flower_garden = ["Rose", "Rose", "Rose", "Rose", "Rose", "Rose"]);
flower_farthest($flower_garden = ["Iris", "Iris"]);