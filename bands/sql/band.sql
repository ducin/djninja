INSERT INTO `band` (`id`, `name`, `active_since`, `active_until`) VALUES
(1, 'Metallica', 1981, NULL),
(2, 'Korn', 1989, NULL),
(3, 'Dio', 1957, 2010),
(4, 'Deep Purple', 1968, NULL),
(5, 'Mother Love Bone', 1988, 1990);

INSERT INTO `band_genres` (`id`, `band_id`, `genre_id`) VALUES
(NULL, '1', '1'),
(NULL, '1', '6'),
(NULL, '2', '6'),
(NULL, '3', '1'),
(NULL, '3', '6'),
(NULL, '4', '1'),
(NULL, '5', '7');
