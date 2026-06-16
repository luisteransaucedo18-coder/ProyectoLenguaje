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
        'https://images.unsplash.com/photo-1511512578047-dfb367046420?auto=format&fit=crop&w=900&q=80',
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
        'https://images.unsplash.com/photo-1585504198199-20277593b94f?auto=format&fit=crop&w=900&q=80',
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
        'https://images.unsplash.com/photo-1542751371-adc38448a05e?auto=format&fit=crop&w=900&q=80',
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
        'https://images.unsplash.com/photo-1550745165-9bc0b252726f?auto=format&fit=crop&w=900&q=80',
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
        'https://images.unsplash.com/photo-1606144042614-b2417e99c4e3?auto=format&fit=crop&w=900&q=80',
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
        'https://images.unsplash.com/photo-1493711662062-fa541adb3fc8?auto=format&fit=crop&w=900&q=80',
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
        'https://images.unsplash.com/photo-1511882150382-421056c89033?auto=format&fit=crop&w=900&q=80',
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
        'https://images.unsplash.com/photo-1579952363873-27f3bade9f55?auto=format&fit=crop&w=900&q=80',
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
        'https://images.unsplash.com/photo-1612287230202-1ff1d85d1bdf?auto=format&fit=crop&w=900&q=80',
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
        'https://images.unsplash.com/photo-1580327344181-c1163234e5a0?auto=format&fit=crop&w=900&q=80',
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
        'https://images.unsplash.com/photo-1560253023-3ec5d502959f?auto=format&fit=crop&w=900&q=80',
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
        'https://images.unsplash.com/photo-1614680376573-df3480f0c6ff?auto=format&fit=crop&w=900&q=80',
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
