CREATE OR REPLACE VIEW active_contracts AS
SELECT
    c.id AS contract_id,
    c.lease_deed,
    c.client_id,
    cl.trade_name AS client_trade_name,
    cl.company_name AS client_company_name,
    c.end_date,
    c.status
FROM contracts c
JOIN clients cl ON c.client_id = cl.id
WHERE c.status = TRUE
    AND NOW() BETWEEN c.start_date AND c.end_date;
