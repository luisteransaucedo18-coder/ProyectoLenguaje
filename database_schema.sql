create table if not exists public.games (
    id text primary key,
    name text not null,
    genre text not null,
    platform text not null,
    mode text not null,
    difficulty text not null,
    duration text not null,
    mood text not null,
    image text not null,
    tags jsonb not null default '[]'::jsonb,
    created_at timestamptz not null default now()
);

alter table public.games enable row level security;

drop policy if exists "Public read games" on public.games;

create policy "Public read games"
on public.games
for select
to anon, authenticated
using (true);

insert into public.games (
    id, name, genre, platform, mode, difficulty, duration, mood, image, tags
)
values
    (
        'zelda_botw',
        'The Legend of Zelda: Breath of the Wild',
        'aventura',
        'nintendo',
        'singleplayer',
        'media',
        'larga',
        'explorar',
        '/static/images/The_Legend_of_Zelda_Breath_of_the_Wild.jpg',
        '["mundo abierto", "fantasia", "exploracion"]'::jsonb
    ),
    (
        'stardew_valley',
        'Stardew Valley',
        'simulacion',
        'pc',
        'ambos',
        'baja',
        'larga',
        'relajarse',
        '/static/images/Stardew Valley.png',
        '["granjas", "cooperativo", "gestion"]'::jsonb
    ),
    (
        'hades',
        'Hades',
        'accion',
        'pc',
        'singleplayer',
        'alta',
        'media',
        'reto',
        '/static/images/Hades.jpg',
        '["roguelike", "mitologia", "combate"]'::jsonb
    ),
    (
        'minecraft',
        'Minecraft',
        'sandbox',
        'pc',
        'ambos',
        'media',
        'larga',
        'crear',
        '/static/images/Minecraft.jpg',
        '["construccion", "supervivencia", "creatividad"]'::jsonb
    ),
    (
        'valorant',
        'Valorant',
        'shooter',
        'pc',
        'multiplayer',
        'alta',
        'corta',
        'competir',
        '/static/images/Valorant.jpg',
        '["tactico", "equipos", "online"]'::jsonb
    ),
    (
        'mario_kart_8',
        'Mario Kart 8 Deluxe',
        'carreras',
        'nintendo',
        'ambos',
        'baja',
        'corta',
        'divertirse',
        '/static/images/Mario Kart 8 Deluxe.jpg',
        '["fiesta", "familia", "competitivo"]'::jsonb
    ),
    (
        'elden_ring',
        'Elden Ring',
        'rpg',
        'playstation',
        'singleplayer',
        'alta',
        'larga',
        'reto',
        '/static/images/Elden Ring.jpg',
        '["soulslike", "mundo abierto", "fantasia"]'::jsonb
    ),
    (
        'fifa_24',
        'EA Sports FC 24',
        'deportes',
        'playstation',
        'ambos',
        'media',
        'corta',
        'competir',
        '/static/images/EA Sports FC 24.jpg',
        '["futbol", "online", "torneos"]'::jsonb
    ),
    (
        'portal_2',
        'Portal 2',
        'puzzle',
        'pc',
        'ambos',
        'media',
        'media',
        'pensar',
        '/static/images/Portal 2.jpg',
        '["puzzles", "historia", "cooperativo"]'::jsonb
    ),
    (
        'animal_crossing',
        'Animal Crossing: New Horizons',
        'simulacion',
        'nintendo',
        'singleplayer',
        'baja',
        'larga',
        'relajarse',
        '/static/images/Animal Crossing New Horizons.jpg',
        '["vida social", "decoracion", "coleccion"]'::jsonb
    ),
    (
        'god_of_war',
        'God of War Ragnarok',
        'accion',
        'playstation',
        'singleplayer',
        'media',
        'media',
        'historia',
        '/static/images/God of War Ragnarok.jpg',
        '["narrativa", "mitologia", "combate"]'::jsonb
    ),
    (
        'among_us',
        'Among Us',
        'social',
        'movil',
        'multiplayer',
        'baja',
        'corta',
        'divertirse',
        '/static/images/AmongUs.jpg',
        '["deduccion", "amigos", "online"]'::jsonb
    )
on conflict (id) do update set
    name = excluded.name,
    genre = excluded.genre,
    platform = excluded.platform,
    mode = excluded.mode,
    difficulty = excluded.difficulty,
    duration = excluded.duration,
    mood = excluded.mood,
    image = excluded.image,
    tags = excluded.tags;
