CREATE TABLE Company (
    ID SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_update_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    api_token VARCHAR(255)
);
CREATE TABLE Document (
    ID SERIAL PRIMARY KEY,
    openID INT NOT NULL,
    token VARCHAR(255) NOT NULL,
    name VARCHAR(255) NOT NULL,
    status VARCHAR(60) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    companyID INT,
    externalID VARCHAR(255),
    FOREIGN KEY (companyID) REFERENCES Company(ID)
);

CREATE TABLE Signers (
    ID SERIAL PRIMARY KEY,
    token VARCHAR(255) NOT NULL,
    status VARCHAR(50) NOT NULL,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    externalID VARCHAR(255),
    documentID INT,
    FOREIGN KEY (documentID) REFERENCES Document(ID)
);