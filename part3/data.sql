-- Insertion de l'administrateur (ID fixe et mot de passe hashé pour 'admin1234')
INSERT INTO users (id, first_name, last_name, email, password, is_admin)
VALUES ('36c9050e-ddd3-4c3b-9731-9f487208bbc1', 'Admin', 'HBnB', 'admin@hbnb.io', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/ZfExtpg.fG.W.XmP.', 1);

-- Insertion des équipements (Amenities) avec des UUID générés
INSERT INTO amenities (id, name) VALUES ('56779831-2911-471a-969c-703666f8e75e', 'WiFi');
INSERT INTO amenities (id, name) VALUES ('9035695a-2e78-43d8-826d-a16086887569', 'Swimming Pool');
INSERT INTO amenities (id, name) VALUES ('17154580-080c-4467-850f-547700234c0f', 'Air Conditioning');
