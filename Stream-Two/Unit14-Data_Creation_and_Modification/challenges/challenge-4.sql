/*/**
 * Since we set the amount of the third entry to
 * 8, we know that 8 x 2 = 16 so we can set the amount to 16
 */
UPDATE `my_db`.`orders` SET amount = 16 WHERE id=3;
 
/**
 * We might not always know what the value of a field is
 * so in that case we will need to the multiplication operator (*)
 * to double the value. In this case we'll need to set `amount = amount * 2`
 */
UPDATE `my_db`.`orders` SET amount = amount * 2 WHERE id=3;