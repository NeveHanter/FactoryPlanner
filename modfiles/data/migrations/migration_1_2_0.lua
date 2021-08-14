local migration = {}

function migration.player_table(player_table)
end

function migration.subfactory(subfactory)
    for _, floor in pairs(Subfactory.get_all_floors(subfactory)) do
        for _, line in pairs(Floor.get_in_order(floor, "Line")) do
            line.ingredient_variants = {}
        end
    end
end

function migration.packed_subfactory(packed_subfactory)
end

return migration
