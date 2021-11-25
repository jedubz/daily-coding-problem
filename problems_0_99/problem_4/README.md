# Daily Coding Problem 4

**Difficulty: Hard**

## Description

Good morning! Here's your coding interview problem for today.

This problem was asked by **[Stripe](https://stripe.com/)**.

Given an array of **integers**, find the first missing positive integer in **linear time** and **constant space**. In other words, find the _lowest_ positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input `[3, 4, -1, 1]` should give `2`. The input `[1, 2, 0]` should give `3`.

You can modify the input array in-place.

## Problem Analysis

### Terms

<dl>
  <dt>Linear Time</dt>
  <dd>The running time of an algorithim increases linearly with the size of the input. The time complexity is O(n).</dd>

  <dt>Constant Space</dt>
  <dd>Memory used in an algorithim does not depend on the size of the input.</dd>
</dl>

### Rules:

1. Generate the lowest positive integer that is not present in an array.
2. Allowed to modify the input array in-place.
3. Not allowed to use memory that is fixed to the size of the input. In other words, declare variables instead of a new array that is n+1 length.
