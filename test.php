<?php

$currentYear = date('Y'); // Get the current year
$seventeenYearsAgo = date('Y', strtotime('-17 years')); // Calculate the year 17 years ago

// Example: If year is between current year and 17 years ago
$year = 2015; // Example year

if ($year >= $seventeenYearsAgo && $year <= $currentYear) {
    echo "The year $year falls within the range from $seventeenYearsAgo to $currentYear.";
} else {
    echo "The year $year does not fall within the range from $seventeenYearsAgo to $currentYear.";
}


?>