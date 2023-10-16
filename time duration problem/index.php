<?php

    // $year = $sec / 31536000;
    // $remainder = $sec % 31536000;


function time_duration($sec)
{
  if($sec <= 60)
  {
     echo $sec."seconds";
  }
  elseif($sec <= 3600)
  {
    $minutes = $sec / 60;
    $seconds = $sec % 60;

    echo "Time duration is :".round($minutes)."minutes".$seconds."seconds";
  }
  elseif($sec <= 86400)
  {
    $hours = floor($sec / 3600);
    $minutes = floor(($sec % 3600) / 60);
    $seconds = $sec - (($hours * 3600) + ($minutes * 60));

    echo "Time duration is :" . round($hours) . "hour " . $minutes . "minutes ". $seconds."seconds";

  }
  elseif($sec <= 604800)
  {
        $days = floor($sec / 86400);
        $hours = floor(($sec % 86400) / 3600);
        $minutes = ($sec - (($days * 86400) + ($hours * 3600))) / 60;

        echo "Time duration is :" . round($days) . "days " . $hours . "hours " . $minutes. "minutes";

  }
  elseif($sec <= 2592000)
  {
        $weeks = floor($sec / 604800);
        $days = floor(($sec % 604800) / 86400);
        $hours = floor(($sec - (($days * 604800) + ($days * 86400))) / (3600*24));
 
        echo "Time duration is :" . $weeks . "weeks " . $days . "days " . $hours . "hours";

  }
  elseif($sec >=  31536000)
  {
        $years = floor($sec / 2592000);
        $months = floor(($sec % 2592000) / 604800);
        $days = floor(($sec - (($years * 25922000) + ($months * 604800))) / (604800));

        echo "Time duration is :" . $years . "years " . $months . "months " . $days . "days";

  }



}

time_duration(176586700);