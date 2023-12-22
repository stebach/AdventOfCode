import os

with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
    text = inputdata.readlines()

lines = slines(text)

class Brick:
    def __repr__(self):
        return self.name

m = {}

bricks = []

for i, line in enumerate(lines):
    a, b = line.split('~')
    a = intlist(a)
    b = intlist(b)
    a = tuple(a)
    b = tuple(b)

    dir = vsub(b, a)
    assert (x >= 0 for x in dir)

    dir = tuple(sgn(x) for x in dir)

    brick = Brick()
    brick.a = a
    brick.b = b
    brick.cos = []
    bricks.append(brick)

    # Name bricks, for checking against the example
    if i < 26:
        brick.name = chr(ord('a') + i)
    else:
        brick.name = str(i)

    # Build brick.cos
    co = a
    while True:
        m[co] = brick
        brick.cos.append(co)

        if co == b:
            break

        co = vadd(co, dir)
        

# Process bottom-up
def zsort(bricks):
    return sorted(bricks, key=lambda brick: brick.a[2])

bricks = zsort(bricks)

down = (0, 0, -1)
up = (0, 0, 1)


def drop(brick, ignore=None):
    dropped = False
    while True:
        blocked = False
        for co in brick.cos:
            next_co = vadd(co, down)
            if next_co[2] == 0:
                blocked = 'gnd'
            elif m.get(next_co) is not None:
                if m.get(next_co) is not brick:
                    if m.get(next_co) is not ignore:
                        blocked = m.get(next_co).name

        if blocked:
            return dropped

        # Move brick down
        for co in brick.cos:
            del m[co]

        brick.cos = [vadd(co, down) for co in brick.cos]

        for co in brick.cos:
            m[co] = brick

        dropped = True

        
for brick in bricks:
    drop(brick)
        

# Visualize to check against example
if 0:
    print('x')
    for z in range(10, 0, -1):
        print(z, end=':')
        for x in range(3):
            b = None
            for y in range(3):
                b = b or m.get((x, y, z))
            if b:
                print(b.name, end='')
            else:
                print('.', end='')
        print('')

    print('y')
    for z in range(10, 0, -1):
        print(z, end=':')
        for y in range(3):
            b = None
            for x in range(3):
                b = b or m.get((x, y, z))
            if b:
                print(b.name, end='')
            else:
                print('.', end='')
        print('')


# Part 1
if 0:
    # Which can be disintegrated
    load_bearers = set()

    for brick in bricks:
        bricks_above = set()

        for co in brick.cos:
            co_above = vadd(co, up)
            brick_above = m.get(co_above)
            if brick_above is not None:
                if brick_above is not brick:
                    bricks_above.add(brick_above)


        for brick_above in bricks_above:
            bricks_below = set()
            for co in brick_above.cos:
                co_below = vadd(co, down)
                brick_below = m.get(co_below)
                if brick_below is not None:
                    if brick_below is not brick_above:
                        bricks_below.add(brick_below)

            assert brick in bricks_below
            if len(bricks_below) == 1:
                load_bearers.add(brick)
                tot += 1
                break

@cache
def chain_length_if_killed(kill_brick):
    global m
    global bricks

    bricks_above = set()

    for co in kill_brick.cos:
        co_above = vadd(co, up)
        brick_above = m.get(co_above)
        if brick_above is not None:
            if brick_above is not kill_brick:
                bricks_above.add(brick_above)


    to_drop = set()

    for brick_above in bricks_above:
        bricks_below = set()
        for co in brick_above.cos:
            co_below = vadd(co, down)
            brick_below = m.get(co_below)
            if brick_below is not None:
                if brick_below is not brick_above:
                    bricks_below.add(brick_below)

        #print('   above is:', brick_above)
        #print('   supported by', bricks_below)
        assert kill_brick in bricks_below
        if len(bricks_below) == 1:
            #print(brick, 'is ok')
            to_drop.add(brick_above)

    if len(to_drop) == 0:
        return 0

    dropped_bricks = set()


    # Save old state
    om = m
    m = dict(m)
    for brick in bricks:
        brick.old_a = brick.a
        brick.old_b = brick.b
        brick.old_cos = list(brick.cos)

    for drop_brick in to_drop:
        if drop(drop_brick, kill_brick):
            dropped_bricks.add(drop_brick)

    dropped_any = False
    for other_brick in bricks:
        if other_brick is not kill_brick:
            if drop(other_brick, brick):
                dropped_any = True
                dropped_bricks.add(other_brick)

    assert kill_brick not in dropped_bricks

    # Restore saved state
    m = om
    for brick in bricks:
        brick.a = brick.old_a
        brick.b = brick.old_b
        brick.cos = brick.old_cos
    return len(dropped_bricks)


ans( sum(chain_length_if_killed(brick) for brick in bricks))
