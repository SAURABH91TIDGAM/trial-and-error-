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
        $hours = floor(($sec - (($weeks * 604800) + ($days * 86400))) / (60 * 60));
 
        echo "Time duration is :" . $weeks . "weeks " . $days . "days " . $hours . "hours";
  }



}

time_duration(1765689);