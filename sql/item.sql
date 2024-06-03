CREATE OR REPLACE FUNCTION get_items(p_project_id INT)
RETURNS TABLE (
    id INT,
    title TEXT,
    article INT,
    description TEXT,
    price NUMERIC(11, 2),
    amount INT
) AS $$
BEGIN
    RETURN QUERY
    SELECT
        i.id,
        i.title,
        i.article,
        i.description,
        i.price,
        s.amount
    FROM
        specifications s
    JOIN
        projects ON projects.id = s.project_id
    JOIN
        items i ON i.id = s.item_id
    WHERE
        s.project_id = p_project_id
    ORDER BY
        i.title;
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION update_specification(p_project_id INT, items INT[][])
RETURNS VOID AS $$
DECLARE
    i INT;
    item_id INT;
    amount INT;
BEGIN
    DELETE FROM
        specifications
    WHERE
        project_id = p_project_id;

    IF array_length(items, 1) IS NULL THEN
        RETURN;
    END IF;

    FOR i IN 1..array_length(items, 1) LOOP
        item_id := items[i][1];
        amount := items[i][2];
        INSERT INTO
            specifications (project_id, item_id, amount)
        VALUES
            (p_project_id, item_id, amount);
    END LOOP;
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION add_item(p_title TEXT, p_article INT, p_description TEXT, p_price NUMERIC(11, 2))
RETURNS INT AS $$
DECLARE
    item_id INT;
BEGIN
    INSERT INTO
        items (title, article, description, price)
    VALUES
        (p_title, p_article, p_description, p_price)
    RETURNING
        id INTO item_id;

    RETURN item_id;
END;
$$ LANGUAGE plpgsql;