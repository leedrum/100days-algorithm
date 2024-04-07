# Hanoi Tower algorithm

- **Mission**
  - We have 3 rods and we must move the tower from the 1st rod to the 3rd rod.

- **Conditions**:
  - Only one disk may be moved at a time.

  - Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack or on an empty rod.

  - No disk may be placed on top of a disk that is smaller than it.

- [**Wiki**](https://en.wikipedia.org/wiki/Tower_of_Hanoi)

## Input

- `height`:
  - description: This is the height of the tower
  - type: `Integer`
  - example: `1`, `2`, `3`

## Output

- Steps to move
  - description: Step will let us know move from where to where
  - type: `String`
  - example: `left to middle`

## How to solve

Just think of it, we need to move the largest disk to right tower, first. For that, we need to move all but this disk to middle tower. Hence we are solving the very same problem [twice] with one less disk.

- To move N disks from left to right:
  - **#1** [recursively] move N-1 disks from left to middle
  - **#2** move largest disk from left to right
  - **#3** [recursively] move N-1 disks from middle to right
